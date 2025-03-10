/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
import daihocmo.Service.QuestionService;
import java.sql.SQLException;
import java.util.List;
import java.util.logging.Level;
import java.util.logging.Logger;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.Assertions;

/**
 *
 * @author admin
 */

public class QuestionTest {
    @Test
    public void test(){
        QuestionService s = new QuestionService();
        
        try {
            List<daihocmo.pojo.Question> questions = s.getQuestion(2);
            Assertions.assertEquals(questions.size(),2);
            
            questions.forEach(s1->System.out.println(s1));
        } catch (SQLException ex) {
            Logger.getLogger(QuestionTest.class.getName()).log(Level.SEVERE, null, ex);
        }
        
    }
}
