#include "Multimedia.h"
#include <ostream>
#include <string>

using namespace std;

Multimedia::Multimedia() : name (""), pathName("") {}

Multimedia::Multimedia(string newName,string newPathName): name(newName),pathName (newPathName) {}

Multimedia::~Multimedia() {}


void Multimedia::setName(string newName) {

    name = newName;
}

void Multimedia::setPathName(string newPathName){

    pathName = newPathName;
}


string Multimedia::getName() const { 
    
    return name;
    
    }


string Multimedia::getPathName() const{ 
    
    return pathName;
    
    }

void Multimedia::display(std::ostream& out)const {
    out << "Le nom du média est : " <<name <<endl ;

    out<<"Le chemin d'accès est : " <<pathName <<endl;
}






