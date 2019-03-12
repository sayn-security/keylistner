import java.beans.XMLEncoder;
import java.io.*;
import java.util.*;
import jxl.*;
import jxl.write.*;
import jxl.write.Number;

public class Master {

	public static void main(String[] args) throws Exception {
		//You will wait 10 seconds after running the program for the box to open where you will
		//type the password
		Thread.sleep(5000);
		String fileName = "Data.xls";
		WritableWorkbook workbook = Workbook.createWorkbook(new File(fileName));
		WritableSheet sheet = workbook.createSheet("Sheet1", 0);
		ArrayList<Double> masterArray = new ArrayList<Double>();
		//change the value of k < 3 to how many times you want the program to run.
		for (int k = 0; k < 3; k++) {
			KeyEventDemo.main(k);
			Extractor z = new Extractor();
			z.reading(k);
			z.splitter();
			ArrayList<Double> hold = new ArrayList<Double>();
			hold = z.holdTimeExtractor();
			ArrayList<Double> flight = new ArrayList<Double>();
			flight = z.flight();
			ArrayList<Double> threeGram = new ArrayList<Double>();
			threeGram = z.threeGram();
			Double total_time = z.totalTime();
			masterArray.clear();
			for (int i = 0; i < hold.size(); i++)
				masterArray.add(hold.get(i));
			for (int i = 0; i < flight.size(); i++)
				masterArray.add(flight.get(i));
			for (int i = 0; i < threeGram.size(); i++)
				masterArray.add(threeGram.get(i));
			masterArray.add(total_time);
			//change the value of sub00 to the current subxx number you are going to use. 
			//Each user is a different subject
			Label label = new Label(0, k + 1, "sub00");
			sheet.addCell(label);
			for (int i = 0; i < masterArray.size(); i++) {
				Number number = new Number(i + 1, k + 1, masterArray.get(i));
				sheet.addCell(number);
			}
			Thread.sleep(10000);
			//You will have 20 seconds to enter the password each time.
			//DO NOT CLOSE THE BOX AFTER YOU TYPE THE PASSWORD. That will end the program and you will
			//have to restart collecting the data for that user.

		}
		workbook.write();
		workbook.close();
	}
}
