import java.io.*;
import java.util.*;

public class Extractor {

	ArrayList<String> a = new ArrayList<String>();
	ArrayList<String> press = new ArrayList<String>();
	ArrayList<Double> pressTime = new ArrayList<Double>();
	ArrayList<String> release = new ArrayList<String>();
	ArrayList<Double> releaseTime = new ArrayList<Double>();
	ArrayList<Double> timings = new ArrayList<Double>();
	
	ArrayList<Double> holdTime = new ArrayList<Double>();
	ArrayList<Double> flightTime = new ArrayList<Double>();
	ArrayList<Double> threeGramTime = new ArrayList<Double>();
	private BufferedReader bc;

	/*public static void main(String[] args) throws IOException {
		Extractor z = new Extractor();
		z.reading();
		z.splitter();
		z.holdTimeExtractor();
		z.flight();
		z.threeGram();
		for (int i = 0; i < z.flightTime.size(); i++) {
			System.out.println(z.flightTime.get(i));
		}
		for (int i = 0; i < z.holdTime.size(); i++) {
			System.out.println(z.holdTime.get(i));
		}
		for (int i = 0; i < z.threeGramTime.size(); i++) {
			System.out.println(z.threeGramTime.get(i));
		}
		
		System.out.println(z.totalTime());
	}*/

	public void reading(int k) throws IOException {
		FileReader ab = new FileReader("out"+k+".txt");
		bc = new BufferedReader(ab);

		String temp;
		while ((temp = bc.readLine()) != null) {
			a.add(temp);
		}
		int countcolon = 0;
		String number = null;
		String temp1;
		double num;
		for (int i = 0; i < a.size(); i++) {
			temp1 = a.get(i);
			for (int j = 0; j < temp1.length(); j++) {
				if (temp1.charAt(j) == ':')
					countcolon++;
				if (countcolon == 2) {
					number = temp1.substring(j + 2);
				}
			}
			num = Double.parseDouble(number);
			if(num < 10.0)
				num = num + 60;
			timings.add(num);
			countcolon = 0;
			number = null;
		}
	}

	public void splitter() {
		String temp;
		int i;
		for (i = 0; i < a.size(); i++) {
			temp = a.get(i);
			if (temp.charAt(4) == 'P') {
				press.add(temp);
				pressTime.add(timings.get(i));
			}
			if (temp.charAt(4) == 'R') {
				release.add(temp);
				releaseTime.add(timings.get(i));
			}
		}
	}

	public ArrayList<Double> holdTimeExtractor() {
		ArrayList<String> TEMP = new ArrayList<String>();
		for (int i = 0; i < a.size(); i++)
			TEMP.add(a.get(i));
		String temp;
		String temp2;
		for (int i = 0; i < press.size(); i++) {
			temp = press.get(i);
			for (int j = 0; j < release.size(); j++) {
				temp2 = release.get(j);
				if (temp.charAt(25) == temp2.charAt(26) && TEMP.contains(release.get(j)) == true) {
					holdTime.add((releaseTime.get(j) - pressTime.get(i)));
					TEMP.remove(release.get(j));
					break;
				}
			}
		}
		return holdTime;
	}

	public ArrayList<Double> threeGram() {
		for (int i = 0; i < press.size() - 3; i++) {
			threeGramTime.add((releaseTime.get(i + 3) - pressTime.get(i)));
		}
		return threeGramTime;
	}

	public double totalTime() {
		return (releaseTime.get(releaseTime.size() - 1) - pressTime.get(0));
	}

	public ArrayList<Double> flight() {
		for (int i = 0; i < pressTime.size() - 1; i++) {
			flightTime.add(releaseTime.get(i) - pressTime.get(i + 1));
		}
		return flightTime;
	}
}
