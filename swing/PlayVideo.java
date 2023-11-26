import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class PlayVideo extends JButton implements ActionListener {
   

    public PlayVideo() {
        super("PlayVideo");

        setBackground(Color.RED);
        setForeground(Color.RED);
        setFocusPainted(false);
        addActionListener(this);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        VideoList videoList = new VideoList();
        videoList.setVisible(true);
            
    }
}
