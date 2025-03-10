/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package daihocmo.Service;

import com.dht.pojo.Choice;
import daihocmo.pojo.JdbcUtils;
import daihocmo.pojo.Question;
import java.lang.reflect.Array;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

/**
 *
 * @author admin
 */
public class QuestionService {
   public List<Question> getQuestion(int limit) throws SQLException{
       List<Question> result = new ArrayList<>();
       try(Connection conn = JdbcUtils.getConn()){
           String sql = "SELECT * FROM question ORDER BY rand() LIMIT ?";
           PreparedStatement stm = conn.prepareCall(sql);
           
           stm.setInt(1, limit);
           
           ResultSet rs = stm.executeQuery();
           
           while (rs.next()) {               
               Question q = new Question(rs.getString("id"), rs.getString("content"), rs.getInt("category_id"));
               
               result.add(q);
               
           }
           return result;
       }
   }
   
   public List<Choice> getChoices(int limit) throws SQLException{
       List<Choice> result = new ArrayList<>();
       try(Connection conn = JdbcUtils.getConn()){
           String sql = "SELECT * FROM choice ORDER BY rand() question_id= ?";
           PreparedStatement stm = conn.prepareCall(sql);
           
           stm.setInt(1, limit);
           
           ResultSet rs = stm.executeQuery();
           
           while (rs.next()) {               
               Choice q = new Choice(rs.getString("id"), rs.getString("content"), rs.getBoolean("is_correct"), rs.getString("question_id"));
               
               result.add(q);
               
           }
           return result;
       }
   }
}
