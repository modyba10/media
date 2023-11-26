import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class PlayPhoto extends JButton implements ActionListener {
   

    public PlayPhoto() {
        super("PlayPhoto");

        setBackground(Color.RED);
        setForeground(Color.RED);
        setFocusPainted(false);
        addActionListener(this);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        System.out.println("nous sommes dans le action performed");
        PhotoList photoList = new PhotoList();
        photoList.setVisible(true);

    }
}