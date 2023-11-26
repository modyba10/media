#ifndef PHOTO_H
#define PHOTO_H

#include "Multimedia.h"
#include <cstdlib>

class Photo : public Multimedia {
public:
    // Constructeurs
    Photo() : latitude(0), longitude(0) {}

    Photo(std::string nName, std::string nPathName, double nlat, double nlong) : Multimedia(nName, nPathName), latitude(nlat), longitude(nlong) {}

    // Constructeur de copie
    Photo(const Photo& other) : Multimedia(other) {
        latitude = other.latitude;
        longitude = other.longitude;
    }

    // Opérateur d'affectation
    Photo& operator=(const Photo& other) {
        if (this != &other) {
            Multimedia::operator=(other);
            latitude = other.latitude;
            longitude = other.longitude;
        }
        return *this;
    }

    // Destructeur
    ~Photo() {
        std::cout << "Photo " << getName() << " is being destroyed." << std::endl;
    }

    // Méthodes de modification de la latitude et de la longitude
    void setLongitude(double nlong) { longitude = nlong; }
    void setLatitude(double nlat) { latitude = nlat; }

    // Méthodes d'obtention de la latitude et de la longitude
    double getLongitude() const { return longitude; }
    double getLatitude() const { return latitude; }

    // Affichage des détails de la photo
    virtual void display(std::ostream& out) const {
        out << "Votre média est une photo" << std::endl;
        out << "Le nom est : " << getName() << std::endl;
        out << "La latitude de votre Photo est : " << latitude << std::endl;
        out << "La longitude de votre Photo est : " << longitude << std::endl;
    }

    // Lecture (ou visualisation) de la photo
    virtual void play() const {
        std::string command = "imagej " + getPathName();
        int status = system(command.c_str());
        if (status != 0) {
            std::cerr << "Erreur lors de l'exécution de la commande." << std::endl;
        }
    }

private:
    double latitude; // Latitude de la photo
    double longitude; // Longitude de la photo
};

#endif
