package day1;

import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void solveDay1() {

        List<String> lines = new ArrayList<>();
        String textFile = "day1/1.txt";
        try {
            lines = java.nio.file.Files.readAllLines(java.nio.file.Paths.get(textFile));
        } catch (java.io.IOException e) {
            e.printStackTrace();
            return;
        }

        int pos = 50;
        int zeros = 0;
        for (String line : lines) {
            String direction = line.substring(0, 1);
            int length = Integer.parseInt(line.substring(1));
            int effectiveTurn = length % 100;
            int boundToAdd = pos == 0 ? 100 : 0;

            pos += effectiveTurn;

            if (pos < 0) {
                zeros += boundToAdd;
                pos = 100 + pos;
            } else if (pos > 99) {
                zeros += boundToAdd;
                pos = pos - 100;
            } else if (pos == 0) {
                zeros += boundToAdd;
            }

            int fullTurns = length / 100;
            zeros += fullTurns;

            System.out.println("Current position: " + pos);
        }

        System.out.println("Number of times at position 0: " + zeros);
    }

    public static void main(String[] args) {
        solveDay1();
    }
}
