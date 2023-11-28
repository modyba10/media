import javax.swing.*;
import java.awt.*;
import java.io.IOException;
import java.net.UnknownHostException;

public class Controller extends JPanel {
  
    private JLabel label; 
    private Client client;
    private PlayVideo playVideo;
    private PlayPhoto playPhoto;
    private BrowseButton browseButton;
    private ExitButton exitButton;

    public Controller() throws UnknownHostException, IOException {
        setLayout(new GridLayout(4, 1)); 
        label = new JLabel("", SwingConstants.CENTER); 
        label.setVerticalAlignment(SwingConstants.TOP); 
        label.setBorder(BorderFactory.createLineBorder(Color.BLACK)); 
        client = new Client(); 

        // Ajout du label au panneau
        add(label);

        // Initialisation du bouton de lecture vidéo
        playVideo = new PlayVideo(); 
        playVideo.setBackground(Color.BLUE);
        playVideo.setForeground(Color.GRAY);

        // Initialisation du bouton de lecture de photo
        playPhoto = new PlayPhoto(); 
        playPhoto.setBackground(Color.BLACK);
        playPhoto.setForeground(Color.GRAY);

        // Initialisation du bouton de parcours
        browseButton = new BrowseButton(client, label); 
        browseButton.setBackground(Color.GREEN); 
        browseButton.setForeground(Color.GRAY);

        // Initialisation du bouton de sortie
        exitButton = new ExitButton();
        exitButton.setBackground(Color.RED); 
        exitButton.setForeground(Color.GRAY);

        // Ajout des différents composants au panneau
        add(playVideo);
        add(playPhoto);
        add(browseButton);
        add(exitButton);
    }
}
