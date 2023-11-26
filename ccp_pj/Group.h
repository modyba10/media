#ifndef GROUP_H
#define GROUP_H

#include <list>
#include <iostream>
#include <memory> // Pour les smart pointers

class Group {
public:
Group(const std::string& groupName) : groupName(groupName) {}

std::string getGroupName() const {
    return groupName;
}

// Ajouter un objet multimédia au groupe en tant que shared_ptr
void addObject(std::shared_ptr<Multimedia> object) {
    objects.push_back(object);
}

// Afficher les attributs de tous les objets du groupe
void displayGroup() const {
    std::cout << "Group Name: " << groupName << std::endl;
    for (const auto& object : objects) {
        object->display(std::cout);
    }
}

void removeObject(std::shared_ptr<Multimedia> object) {
    auto it = std::find(objects.begin(), objects.end(), object);
    if (it != objects.end()) {
        objects.erase(it);
    }
}

private:
std::string groupName;
std::list<std::shared_ptr<Multimedia>> objects;
};


#endif