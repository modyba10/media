# Nom du programme
CLIENT=client
SERVER=server

# Fichiers sources
CLIENT_SOURCES=client.cpp ccsocket.cpp 
SERVER_SOURCES=Multimedia.cpp MediaManager.cpp server.cpp tcpserver.cpp ccsocket.cpp 

# Compilateur C++
CXX= g++
CXXFLAGS= -std=c++11 -Wall -g
LDLIBS= -lpthread

# Règles de construction
all: ${CLIENT} ${SERVER}

${CLIENT}: ${CLIENT_SOURCES}
	${CXX} -o $@ ${CXXFLAGS} ${CLIENT_SOURCES} ${LDLIBS}

${SERVER}: ${SERVER_SOURCES}
	${CXX} -o $@ ${CXXFLAGS} ${SERVER_SOURCES} ${LDLIBS}

# Règle pour exécuter le serveur
run: ${SERVER}
	./${SERVER}

clean:
	rm -f ${CLIENT} ${SERVER}
