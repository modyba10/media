#ifndef FILM_H
#define FILM_H

#include "Video.h"
#include <string>
#include <iostream>

class Film : public Video {
public:
Film() : Video(), numberOfChapters(0), chapters(nullptr) {}

Film(std::string name, std::string pathName, int duration, int numChapters, int* nChapters)
: Video(name, pathName, duration), numberOfChapters(numChapters) {
chapters = new int[numChapters];
for (int i = 0; i < numChapters; ++i) {
    chapters[i] = nChapters[i];
}
}

~Film() {

delete[] chapters;
std::cout << "Film " << getName() << " is being destroyed." << std::endl; 
}

Film(const Film& other) : Video(other), numberOfChapters(other.numberOfChapters) {
chapters = new int[other.numberOfChapters];
for (int i = 0; i < other.numberOfChapters; ++i) {
    chapters[i] = other.chapters[i];
}
}

Film& operator=(const Film& other) {
if (this != &other) {
Video::operator=(other); // Appel de l'opérateur d'assignation de la classe de base
delete[] chapters; // Libérer l'ancien tableau s'il existe
numberOfChapters = other.numberOfChapters;
chapters = new int[other.numberOfChapters];
for (int i = 0; i < other.numberOfChapters; ++i) {
    chapters[i] = other.chapters[i];
}
}
return *this;
}


int getNumberOfChapters() const {
return numberOfChapters;
}

int* getChapters() const {
return chapters;
}

void setNumberOfChapters(int newNumber) {
numberOfChapters = newNumber;
}

void setChapters(int* nChapters, int nNumChapters) {

// Libérer l'ancien tableau si présent

delete[] chapters;

// Allouer un nouveau tableau et copier les données

if (nChapters != nullptr && nNumChapters > 0) {

    chapters = new int[nNumChapters];

    for (int i = 0; i < nNumChapters; ++i) {
        chapters[i] = nChapters[i];
    }
    numberOfChapters = nNumChapters;

} else {
    chapters = nullptr;
    numberOfChapters = 0;
}
}

virtual void display(std::ostream& out) const{
    std::cout << "Votre média est un film" << std::endl;;
std::cout << "Nom : " << getName() << std::endl;
std::cout << "Chemin : " << getPathName() << std::endl;
std::cout << "Durée : " << getDuration() << " secondes" << std::endl;
std::cout << "Nombre de chapitres : " << numberOfChapters << std::endl;
for (int i = 0; i < numberOfChapters; i++) {
    std::cout << "Chapitre " << i + 1 << " Durée du chapitre : " << chapters[i] << " secondes" << std::endl;
}
}

private:
int numberOfChapters;
int* chapters;
};

#endif
