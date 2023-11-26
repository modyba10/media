#ifndef VIDEO_H
#define VIDEO_H

#include "Multimedia.h"

class Video : public Multimedia {
public:
    // Constructeurs
    Video() : Multimedia("No Name", "No Path"), duration(0) {}

    Video(std::string nName, std::string nPathName, int nDuration) : Multimedia(nName, nPathName), duration(nDuration) {}
    
    // Destructeur
    virtual ~Video() {
        std::cout << "Video " << getName() << " is being destroyed." << std::endl;
    }

    // Méthodes d'obtention et de définition de la durée de la vidéo
    int getDuration() const { return duration; }
    void setDuration(int nDuration) { duration = nDuration; }

    // Affichage des détails de la vidéo
    virtual void display(std::ostream& out) const {
        out << "Votre média est une vidéo" << std::endl;
        std::cout << "Nom : " << getName() << std::endl;
        out << "Durée : " << duration << " secondes" << std::endl;
    }

    // Lecture (ou visualisation) de la vidéo
    virtual void play() const {
        std::string command = "mpv \"" + getPathName() + "\" &";
        int status = system(command.c_str());
        if (status != 0) {
            std::cerr << "Erreur lors de l'exécution de la commande." << std::endl;
        }
    }

private:
    int duration; // Durée de la vidéo en secondes
};

#endif
