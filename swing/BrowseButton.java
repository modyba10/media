import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.io.*;

import javax.swing.filechooser.FileNameExtensionFilter;

public class BrowseButton extends JButton implements ActionListener {
    private static final long serialVersionUID = 1L;
    private JLabel displayLabel;
    private Client client;

    public BrowseButton(Client client, JLabel displayLabel) {
        super("Browse");
        setBackground(Color.RED);
        this.displayLabel = displayLabel;
        this.client = client;
        setForeground(Color.RED);
        setFocusPainted(false);
        addActionListener(this); // Ajout de l'écouteur d'événements
    }
    
    /**
     * Méthode appelée lorsqu'un événement est déclenché, dans ce cas,
     * lorsque le bouton de parcours est cliqué pour sélectionner un fichier.
     * Elle ouvre une boîte de dialogue de sélection de fichier et envoie
     * les informations du fichier sélectionné au serveur.
     * @param e L'événement d'action associé à cette méthode
     */
    @Override
    public void actionPerformed(ActionEvent e) {
        JFileChooser fileChooser = new JFileChooser();
        FileNameExtensionFilter filter = new FileNameExtensionFilter("Media Files", "jpg", "png", "gif", "mp4");
        fileChooser.setFileFilter(filter);
    
        int returnValue = fileChooser.showOpenDialog(null);
    
        if (returnValue == JFileChooser.APPROVE_OPTION) {
            File selectedFile = fileChooser.getSelectedFile();
            // Obtention du chemin, nom et type de fichier
            String filePath = selectedFile.getPath();
            String fileName = selectedFile.getName();
            int mediaType = determineMediaType(fileName);
    
            // Envoi au serveur
            sendToServer(filePath, fileName, mediaType);
            displayLabel.setText("Nom du média:" + fileName);
        }
    }
    
    /**
     * Détermine le type de média en fonction de l'extension du fichier.
     * @param fileName Le nom du fichier
     * @return Le type de média (0 pour une photo, 1 pour une vidéo, -1 si le type n'est pas pris en charge)
     */
    private int determineMediaType(String fileName) {
        String extension = fileName.substring(fileName.lastIndexOf(".") + 1);
    
        // Déterminer le type de média en fonction de l'extension du fichier
        if (extension.equalsIgnoreCase("jpg") || extension.equalsIgnoreCase("png") || extension.equalsIgnoreCase("gif")) {
            return 0; // Photo
        } else if (extension.equalsIgnoreCase("mp4") || extension.equalsIgnoreCase("avi")) {
            return 1; // Vidéo
        } else {
            return -1; // Type non pris en charge
        }
    }
    
    /**
     * Envoie les informations du fichier sélectionné au serveur.
     * @param filePath   Le chemin du fichier
     * @param fileName   Le nom du fichier
     * @param mediaType  Le type de média (photo, vidéo, ou non pris en charge)
     */
    private void sendToServer(String filePath, String fileName, int mediaType) {
        if (client != null) {
            String message = filePath + ";" + fileName + ";" + mediaType;
    
            // Envoi du message au serveur en utilisant la méthode send de l'instance de Client
            String response = client.send(message);
    
            if (response != null) {
                System.out.println("Server response: " + response);
            } else {
                System.out.println("No response from server.");
            }
        } else {
            System.out.println("Client instance is null.");
        }
    }
    
    
}
