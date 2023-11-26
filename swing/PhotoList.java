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
            client = new Client(); 
        } catch (Exception e) {
            e.printStackTrace();
        }
        

        setTitle("PhotoList");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout());

        
        String[] mediaNames = fetchMediaListFromServer();

        mediaList = new JComboBox<>(mediaNames);
        mediaList.addActionListener(this);
        

        add(mediaList, BorderLayout.CENTER);
        

        pack();
        
        setLocationRelativeTo(null);
        
        setVisible(true);
    }


    private String[] fetchMediaListFromServer() {
     
        String response = client.send("GetAllPhoto");
        
        

        
        return response.split(","); 
    }

    
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == mediaList) {
            String selectedMedia = (String) mediaList.getSelectedItem();
            try {
                client =new Client();
            } catch (IOException e1) {
            
                e1.printStackTrace();
            }
            
            String confirmation = client.send(selectedMedia);
            

        }
    }

}



