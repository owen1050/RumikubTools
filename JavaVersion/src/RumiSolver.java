import org.apache.commons.math3.util.CombinatoricsUtils;

import java.util.*;

public class RumiSolver {

    public static void main(String[] args) {
        printSolution();
    }
//##TODO## remove all in make all combos which dont have all tiles in deck
    public static void test(){
        int[][] ddi = make_all_combos();
        for (int i = 0; i < ddi.length; i++) {
            for (int j = 0; j < ddi[i].length; j++) {
                System.out.print(ddi[i][j] + ":");
            }
            System.out.println("");
        }

    }

    public static void printSolution(){
        int[][] ddi = make_all_combos();
        int[] deck = new int [] {2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1};
        //15949 - int[] deck = new int [] {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 2, 2, 2, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 2, 2, 1};

        List<int[]> hands = new ArrayList<>();

        long now = System.currentTimeMillis();
        List<int[]> ans = null;
        for(int i = 0; i < 1;i++){

            ans = solve(hands, deck, ddi);
        }
        long diff = System.currentTimeMillis()-now;

        if(ans == null || ans.size() == 0){
            System.out.println("No solution");
        } else {
            for (int i = 0; i < ans.size(); i++) {
                for (int j = 1; j <= ans.get(i)[0]; j++) {
                    System.out.print(ans.get(i)[j] + ":");
                }
                System.out.println("");
            }
        }
        System.out.println("Time for 1 mil = "+diff);
    }

    public static int[][] make_all_combos() {
        int[][] ret = new int[185][6];
        int ix  = 0;
        int c;
        //straights first
        for(int cT = 0; cT < 4; cT++) {
            c = 13 * cT;
            for(int i = 0; i < 13; i++) {
                for(int j = 0; j < 13; j++) {
                    if(i + j < 13 && j >= 2 && j < 5) {
                        ret[ix][0] = j + 1;
                        for(int k = 1; k <= j + 1; k++) {
                            ret[ix][k] = c + k + i - 1;
                        }
                        ix++;
                    }
                }
            }
        }

        int[][] combs = new int[4][3];
        Iterator<int[]> iterator = CombinatoricsUtils.combinationsIterator(4,3);
        int i = 0;
        while (iterator.hasNext()) {
            final int[] combination = iterator.next();
            combs[i] = combination;
            i = i + 1;
        }

        for(i = 0; i < 13; i++) {
            for(int j = 0; j < 4; j++){
                ret[ix][0] = 3;
                for(int k = 0; k < 3; k++) {
                    ret[ix][k+1] = i + combs[j][k] * 13;
                }
                ix++;
            }
            ret[ix][0] = 4;
            for(int k = 0; k < 4; k++) {
                ret[ix][k+1] = k * 13 + i;
            }
            ix++;
        }
        return ret;
    }

    public static boolean isHandInDeck(int[] combo, int[] deck){
        int[] tempDeck = deck.clone();
        for(int i = 1; i < combo[0]; i++){
            if(tempDeck[combo[i]] > 0){
                tempDeck[combo[i]] = tempDeck[combo[i]] - 1;
            } else {
                return false;
            }
        }
        return true;
    }

    public static int[] removeHandReturnNewDeck(int[] combo, int[] deck){
        int[] tempDeck = deck.clone();
        for(int i = 1; i <= combo[0]; i++){
            if(tempDeck[combo[i]] > 0){
                tempDeck[combo[i]] = tempDeck[combo[i]] - 1;
            }
        }
        return tempDeck;
    }

    public static void printDeck(int[] deck){
        for(int i = 0; i < deck.length; i++){
            System.out.print(":"+deck[i]);
        }
        System.out.println("");
    }
    public static void printHands(List<int[]> hand){
        for(int j =0; j<hand.size();j++) {
            for (int i = 0; i < hand.get(j).length; i++) {
                System.out.print(":" + hand.get(j)[i]);
            }
            System.out.println("");
        }
    }

    public static boolean isBoardPossible(int[] deck){
        boolean allPossible = true;
        boolean thisRunPoss = false;
        int num, count;
        int[] flush;
        for(int i = 0; i < deck.length; i++){
            if(deck[i] > 0){
                thisRunPoss = false;
                count = 0;
                num = i % 13;
                flush = new int[] {num, num + 13, num + 26, num + 39};
                //System.out.println(num + ":" + i);
                try{
                    if(num == 0 && deck[i+1] > 0 && deck[i+2] > 0) thisRunPoss = true;
                    else if(num == 12 && deck[i-1] > 0 && deck[i-2] > 0) thisRunPoss = true;
                    else if(num == 1){
                        if((deck[i-1] > 0 && deck[i+1] > 0) || (deck[i+1] > 0 && deck[i+2] > 0)) thisRunPoss = true;
                    }
                    else if(num == 11 && (deck[i-1] > 0 && deck[i+1] > 0) || (deck[i-1] > 0 && deck[i-2] > 0)) thisRunPoss = true;
                    else if((deck[i-1] > 0 && deck[i+1] > 0) || (deck[i-1] > 0 && deck[i-2] > 0) || (deck[i+2] > 0 && deck[i+1] > 0)) thisRunPoss = true;
                } catch (Exception e){}

                for(int j = 0; j < 4; j++){
                    if(deck[flush[j]] > 0){
                        count++;
                    }
                }
                if(count > 2) thisRunPoss = true;
                if(!thisRunPoss) {
                    allPossible = false;
                    break;
                }
            }
        }
        return allPossible;
    }

    public static List<int[]> solve(List<int[]> hands, int[] deck, int[][] allCombos){
        boolean isEmpty = true;
        for(int i = 0; i < 52; i ++){
            if(deck[i] > 0){
                isEmpty = false;
                break;
            }
        }
        if(isEmpty){
            return hands;
        }
        if(!isBoardPossible(deck)){
            return null;
        }
        for(int i = 0; i < 185; i++){
            if(isHandInDeck(allCombos[i], deck)){
                List<int[]> newHand = new ArrayList<>(hands);
                newHand.add(allCombos[i]);
                List<int[]> ans = solve(newHand, removeHandReturnNewDeck(allCombos[i], deck), allCombos);
                if(ans != null){
                    return ans;
                }
            }
        }
        return null;
    }
}