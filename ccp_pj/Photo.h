#ifndef PHOTO_H
#define PHOTO_H

#include "Multimedia.h"
 
#include <cstdlib>


class Photo : public Multimedia {


public:


    Photo() : latitude(0), longitude(0) {}

    Photo(std::string nName, std::string nPathName,double nlat, double nlong) : Multimedia(nName,nPathName), latitude(nlat), longitude(nlong) {}

   
   
    Photo(const Photo& other) : Multimedia(other) {
        latitude = other.latitude;
        longitude = other.longitude;
    }

    

    Photo& operator=(const Photo& other) {
        if (this != &other) {
            Multimedia::operator=(other);
            latitude = other.latitude;
            longitude = other.longitude;
        }
        return *this;
    }


    
    ~Photo() {
        std::cout << "Photo " << getName() << " is being destroyed." << std::endl;
    }



    void setLongitude(double nlong) { longitude = nlong; }

    void setLatitude(double nlat) { latitude = nlat; }






    double getLongitude() const { return longitude; }

    double getLatitude() const { return latitude; }





    virtual void display(std::ostream& out) const {
        out << "Votre média est une photo" << std::endl; 
        out << "Le nom est :" <<getName() <<std::endl;
        out << "La latitude de votre Photo est : " << latitude << std::endl; 
        out << "La longitude de votre Photo est : " << longitude << std::endl; 
    }




    virtual void play() const {

    std::string command = "imagej " + getPathName();


    int status = system(command.c_str());

    if (status != 0) {

        std::cerr << "Erreur lors de l'exécution de la commande." << std::endl;

    }


    }

private:
    double latitude;
    double longitude;
};

#endif
