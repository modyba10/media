#ifndef MULTIMEDIA_H
#define MULTIMEDIA_H

#include <string>
#include <ostream>


class Multimedia {

    public :

    Multimedia () ;
    Multimedia (std::string name,std::string pathName);
    virtual~Multimedia () ;

    void setName (std::string newName);
    void setPathName(std::string newpathName);


    std::string getName () const ;
    std::string getPathName() const;


    virtual void display (std::ostream& out) const;

    virtual void play () const =0 ;


    private:

    std::string name;
    std::string pathName;

};

#endif