import java.awt.BorderLayout;
import java.awt.Point;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.event.MouseMotionAdapter;
import java.awt.Graphics;

import java.util.ArrayList;
import java.util.List;

import javax.swing.SwingUtilities;
import javax.swing.JFrame;
import javax.swing.JPanel;

import javax.imageio.ImageIO;
import javax.swing.WindowConstants;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

public class RenderEngine extends JPanel{
    	public static void main(String[] args) throws IOException {
        	JFrame frame = buildFrame();
		RenderEngine instance = new RenderEngine();

        	final BufferedImage[] image = {ImageIO.read(new File("images/character.png"))}; // Error: cannot find image
		int[] x = {0};
		int[] y = {0};

        	JPanel pane = new JPanel() {
            		protected void paintComponent(Graphics g) {
				for (int i = 0; i < image.length; i++) {
  					g.drawImage(image[i], x[i], y[i], null);
				}
            		}
        	};
        	frame.add(pane);

		//Main Loop
		while(true){
			try {
  				Thread.sleep(10);
			} catch (InterruptedException e) {
  				Thread.currentThread().interrupt();
			}
			x[0]+=1;
        		instance.redo(frame);
		}
    	}
	private void redo(JFrame frame){
		repaint(0, 0, getWidth(), getHeight());
		SwingUtilities.updateComponentTreeUI(frame);
	}

    	private static JFrame buildFrame() {
        	JFrame frame = new JFrame();
        	frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        	frame.setSize(1000, 1000);
        	frame.setVisible(true);
        	return frame;
    	}
}