module daihocmo.englishapp {
    requires javafx.controls;
    requires javafx.fxml;
    requires java.sql;

    opens daihocmo.englishapp to javafx.fxml;
    exports daihocmo.englishapp;
    exports daihocmo.Service;
    exports daihocmo.pojo;
}
