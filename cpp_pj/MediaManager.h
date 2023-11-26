#ifndef MEDIAMANAGER_H
#define MEDIAMANAGER_H

#include <iostream>
#include <map>
#include <memory>
#include "Photo.h"
#include "Video.h"
#include "Film.h"
#include "Group.h"

class MediaManager {
public:


    // Méthodes de création

    MediaManager();
    ~MediaManager();
    std::shared_ptr<Photo> createPhoto(const std::string& name, const std::string& path, double latitude, double longitude);
    std::shared_ptr<Video> createVideo(const std::string& name, const std::string& path, int duration);
    std::shared_ptr<Film> createFilm(const std::string& name, const std::string& path, int duration, int numChapters, int* chapters);
    std::shared_ptr<Group> createGroup(const std::string& name);

    // Méthodes pour afficher et jouer un média, afficher le contenu d'un groupe
    std::shared_ptr<Multimedia> findMedia(const std::string& name) const;
    void displayMedia(const std::string& name) const;
    void playMedia(const std::string& name) const;
    const std::map<std::string, std::shared_ptr<Multimedia>>& getMediaTable() const;
    void displayGroup(const std::string& name) const;

    // Méthodes de suppression
    void removeMedia(const std::string& name);
    void removeGroup(const std::string& name);

private:
    std::map<std::string, std::shared_ptr<Multimedia>> mediaTable;
    std::map<std::string, std::shared_ptr<Group>> groupTable;
};

#endif // MEDIAMANAGER_H
