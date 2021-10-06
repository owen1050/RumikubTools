import org.apache.commons.math3.util.CombinatoricsUtils;

import java.util.*;

public class RumiSolver {
    int[][] allCombos;
    Map<int[], Integer> longCombos;

    public void main() {
        this.allCombos = make_all_combos();
        //this.longCombos = getLongMap();
        //printSolution();
        runAll();
    }

    public  int incArray(int[] arr, int max){
        int x = arr.length - 1;
        while(arr[x] == max){
            arr[x] = 0;
            x--;
        }
        arr[x] = arr[x] + 1;
        return x;
    }

    public void runAll(){

        int[] deck = new int [] {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 2, 2, 2, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 2, 2, 1};
        for(int i = 0; i < 52; i++){
            deck[i] = 0;
        }
        List<int[]> hands = new ArrayList<>();
        int count = 0;
        long now = System.currentTimeMillis();
        List<int[]> ans = null;
        long diff = System.currentTimeMillis()-now;
        int lastDiff = 0;
        while(incArray(deck, 2) > 0){
            if((int)(diff /1000) != lastDiff){
                lastDiff=(int)(diff/1000);
                printDeck(deck);
            }
            diff = System.currentTimeMillis()-now;
        }
        diff = System.currentTimeMillis()-now;

        System.out.println("Time for 1 mil = "+diff);
    }

    public void printSolution(){
        int[] deck = new int [] {2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2,1,1,2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2};
        //int[] deck = new int [] {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 2, 2, 2, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 2, 2, 1};
        for(int i = 0; i < 52; i++){
            //deck[i] = 0;
        }

        List<int[]> hands = new ArrayList<>();

        long now = System.currentTimeMillis();
        List<int[]> ans = null;
        for(int i = 0; i < 1;i++){
            ans = solve(hands, deck);
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

    public int[][] make_all_combos() {
        int[][] ret = new int[329][14];
        int ix  = 0;
        int c;
        //straights first
        for(int cT = 0; cT < 4; cT++) {
            c = 13 * cT;
            for(int i = 0; i < 13; i++) {
                for(int j = 0; j < 13; j++) {
                    if(i + j < 13 && j >= 2 && j < 13) {
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

    public boolean isHandInDeck(int[] combo, int[] deck){
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

    public int[] removeHandReturnNewDeck(int[] combo, int[] deck){
        int[] tempDeck = deck.clone();
        for(int i = 1; i <= combo[0]; i++){
            if(tempDeck[combo[i]] > 0){
                tempDeck[combo[i]] = tempDeck[combo[i]] - 1;
            }
        }
        return tempDeck;
    }

    public  void printDeck(int[] deck){
        for(int i = 0; i < deck.length; i++){
            System.out.print(":"+deck[i]);
        }
        System.out.println("");
    }
    public  void printHands(List<int[]> hand){
        for(int j =0; j<hand.size();j++) {
            for (int i = 0; i < hand.get(j).length; i++) {
                System.out.print(":" + hand.get(j)[i]);
            }
            System.out.println("");
        }
    }

    public  boolean isBoardPossible(int[] deck){
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

    public  List<int[]> solve(List<int[]> hands, int[] deck){
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
            if(isHandInDeck(this.allCombos[i], deck)){
                List<int[]> newHand = new ArrayList<>(hands);
                newHand.add(this.allCombos[i]);
                List<int[]> ans = solve(newHand, removeHandReturnNewDeck(this.allCombos[i], deck));
                if(ans != null){
                    return ans;
                }
                else
                {
                    for(int jk:deck){
                        System.out.print(jk+":");
                    }
                    System.out.println("");
                }
            }
        }
        return null;
    }


    public  Map<int[], Integer> getLongMap(){
        int[][] ret = new int[329][14];
        int ix  = 0;
        int c;
        //straights first
        for(int cT = 0; cT < 4; cT++) {
            c = 13 * cT;
            for(int i = 0; i < 13; i++) {
                for(int j = 0; j < 13; j++) {
                    if(i + j < 13 && j >= 2 && j < 13) {
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
        Map<int[], Integer> allLongCombos = new HashMap<int[], Integer>();
        int w = 0;
        for(int[] hand: ret){
            for(int q:hand){
                System.out.print(":" + q);
            }
            System.out.println("---" +w );
            w++;
            allLongCombos.put(hand, 1);
        }
        return allLongCombos;

    }
}