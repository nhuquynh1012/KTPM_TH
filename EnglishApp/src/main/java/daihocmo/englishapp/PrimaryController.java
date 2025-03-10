package daihocmo.englishapp;

import java.io.IOException;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Alert;
import javafx.scene.control.ButtonType;

public class PrimaryController {

    public void addHandder(ActionEvent e){
        Alert alert = new Alert(Alert.AlertType.INFORMATION, "Hello friend", ButtonType.OK);
        alert.show();
    }
}
