#include <memory>
#include <string>
#include <iostream>
#include <sstream>
#include "tcpserver.h"
#include "MediaManager.h"
#include <fstream>
#include <algorithm>

const int PORT = 3331;

int main(int argc, char* argv[]) {
    MediaManager manager;

    // Gestion du contenu multimedia
    std::shared_ptr<Photo> photo1 = manager.createPhoto("Vacances", "cpp_pj/F5GXNMZXkAAaQJC.jpeg", 40.0, 50.0);
    std::shared_ptr<Video> video1 = manager.createVideo("Anniversaire", "music.mp4", 120);
    




// Reponse du serveur au differentes requettes des clients

    auto* server = new TCPServer([&](std::string const& request, std::string& response) {
        try {
            if (request == "GetAllVideo") {
                std::string videoNames;

                // Parcourir la table mediaTable pour récupérer les noms des vidéos
                for (const auto& pair : manager.getMediaTable()) {
                    std::shared_ptr<Video> video = std::dynamic_pointer_cast<Video>(pair.second);
                    if (video) {
                        if (!videoNames.empty()) {
                            videoNames += ",";
                        }
                        videoNames += video->getName();
                    }
                }

                // Envoyer la liste des noms des vidéos en réponse
                response = videoNames;
                return true;
            }
            if (request == "GetAllPhoto") {
                
                std::string photoNames;

                // Parcourir la table mediaTable pour récupérer les noms des photo
                for (const auto& pair : manager.getMediaTable()) {
                    std::shared_ptr<Photo> photo = std::dynamic_pointer_cast<Photo>(pair.second);
                    if (photo) {
                        if (!photoNames.empty()) {
                            photoNames += ",";
                        }
                        photoNames += photo->getName();
                    }
                }

                // Envoyer la liste des noms des photos en réponse
                response = photoNames;
                return true;
            }

            std::cout << "Received request: " << request << std::endl;

            // Vérifier si la requête contient exactement deux points-virgules
            int countSemicolons = std::count(request.begin(), request.end(), ';');

            if (countSemicolons <2) {

                manager.playMedia(request);
                response = "Le media est en train d'être joué avec succès" ;
            }

            if (countSemicolons == 2) {
                std::istringstream iss(request);
                std::string filePath, fileName, mediaTypeStr;
                std::getline(iss, filePath, ';');
                std::getline(iss, fileName, ';');
                std::getline(iss, mediaTypeStr, ';');
                int mediaType = std::stoi(mediaTypeStr);

                
                std::cout << "File Path: " << filePath << std::endl;
                std::cout << "File Name: " << fileName << std::endl;
                std::cout << "Media Type: " << mediaType << std::endl;

                
            if (mediaType == 0) {
                    std::shared_ptr<Photo> photo = manager.createPhoto(fileName, filePath, 0.0, 0.0);
                    
                    std::cout << "Created photo: " << fileName << std::endl;

                    // Jouez le média
                    manager.playMedia(fileName);
                    response = "Tout est OK";

            } else if (mediaType == 1) {
                    std::shared_ptr<Video> video = manager.createVideo(fileName, filePath, 0);
                    std::cout << "Created video: " << fileName << std::endl;
                    manager.playMedia(fileName);
                    response = "Tout est OK";
                }

                return true;
            }
            else {
            
            response = "Erreur";
            return false; 
        }
         

        } catch (const std::exception& e) {
            // Gérez l'exception ici, vous pouvez imprimer un message d'erreur ou effectuer d'autres actions nécessaires
            std::cerr << "Error: " << e.what() << std::endl;
            response = "Erreur lors du traitement de la requête";
            return false; // Pour interrompre la connexion avec le client en cas d'erreur
        }
    });

    // Lancez la boucle infinie du serveur
    std::cout << "Starting Server on port " << PORT << std::endl;

    int status = server->run(PORT);

    // En cas d'erreur lors du démarrage du serveur
    if (status < 0) {
        std::cerr << "Could not start Server on port " << PORT << std::endl;
        delete server; // Libération de la mémoire allouée pour le serveur en cas d'erreur
        return 1;
    }

    return 0;
}
