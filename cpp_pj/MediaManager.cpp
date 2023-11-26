#include "MediaManager.h" 


MediaManager::MediaManager () {}
MediaManager::~MediaManager() {}

// Méthodes de création

std::shared_ptr<Photo> MediaManager::createPhoto(const std::string& name, const std::string& path, double latitude, double longitude) {
auto photo = std::make_shared<Photo>(name, path, latitude, longitude);
mediaTable[name] = photo;
return photo;
}

std::shared_ptr<Video> MediaManager::createVideo(const std::string& name, const std::string& path, int duration) {
auto video = std::make_shared<Video>(name, path, duration);
mediaTable[name] = video;
return video;
}

std::shared_ptr<Film> MediaManager::createFilm(const std::string& name, const std::string& path, int duration, int numChapters, int* chapters) {
auto film = std::make_shared<Film>(name, path, duration, numChapters, chapters);
mediaTable[name] = film;
return film;
}

std::shared_ptr<Group> MediaManager::createGroup(const std::string& name) {
auto group = std::make_shared<Group>(name);
groupTable[name] = group;
return group;
}

// Méthodes pour rechercher, afficher et jouer un média, afficher le contenu d'un groupe

std::shared_ptr<Multimedia> MediaManager::findMedia(const std::string& name) const {

auto it = mediaTable.find(name);
if (it != mediaTable.end()) {

    std::cout << "On a trouvé le media" <<std::endl;
    return it->second;

} else {
    return nullptr;
}
}


const std::map<std::string, std::shared_ptr<Multimedia>>&  MediaManager::getMediaTable() const {
        return mediaTable;
    }

void MediaManager::displayMedia(const std::string& name) const {
std::shared_ptr<Multimedia> media = findMedia(name);
if (media != nullptr) {
    media->display(std::cout);
} else {
    std::cout << "Media not found." << std::endl;
}
}


void MediaManager::playMedia(const std::string& name) const {
auto it = mediaTable.find(name);
if (it != mediaTable.end()) {
    it->second->play();
} else {
    std::cout << "Media not found." << std::endl;
}
}


 

void MediaManager::displayGroup(const std::string& name) const {
auto it = groupTable.find(name);
if (it != groupTable.end()) {
    it->second->displayGroup();
} else {
    std::cout << "Group not found." << std::endl;
}
}



// Méthodes de suppression

void MediaManager::removeMedia(const std::string& name) {
auto it = mediaTable.find(name);
if (it != mediaTable.end()) {
    mediaTable.erase(it);
} else {
    std::cout << "Media not found." << std::endl;
}
}

void MediaManager::removeGroup(const std::string& name) {
auto it = groupTable.find(name);
if (it != groupTable.end()) {
    groupTable.erase(it);
} else {
    std::cout << "Group not found." << std::endl;
}
}
