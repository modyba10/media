import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.IOException;

public class PhotoList extends JFrame implements ActionListener {
    private JComboBox<String> mediaList;
    private Client client;

    public PhotoList() {
        try {
            client = new Client(); // Initialisation du client pour la communication avec le serveur
        } catch (Exception e) {
            e.printStackTrace();
        }
        
        setTitle("PhotoList");
        
        setLayout(new BorderLayout());

        // Récupération de la liste des médias depuis le serveur
        String[] mediaNames = fetchMediaListFromServer();

        // Création de la liste déroulante pour afficher les médias
        mediaList = new JComboBox<>(mediaNames);
        mediaList.addActionListener(this);

        // Ajout de la liste déroulante au cadre
        add(mediaList, BorderLayout.CENTER);

        pack(); 

        setLocationRelativeTo(null); 

        setVisible(true); 
    }

    // Méthode pour récupérer la liste des médias depuis le serveur
    private String[] fetchMediaListFromServer() {
        String response = client.send("GetAllPhoto"); 
        
        return response.split(",");
    }

    // Gestionnaire d'événements pour les actions sur la liste déroulante
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == mediaList) {
            String selectedMedia = (String) mediaList.getSelectedItem(); 

            try {
                client = new Client(); 
            } catch (IOException e1) {
                e1.printStackTrace();
            }

            // Envoi du média sélectionné au serveur et affichage de la réponse
            String confirmation = client.send(selectedMedia);
            System.out.println(confirmation);
        }
    }
}
