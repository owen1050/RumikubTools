import org.apache.commons.math3.util.CombinatoricsUtils;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;



public class RumiSolverByCombo {
    int[][] allCombos;

    public void run() {
        int[][] hands = new int[0][0];
        allCombos = make_all_combos();
        solve(hands);
    }

    public void solve(int[][] hands){
        for(int[] hand: allCombos){
            int[][] newHands = new int[hands.length + 1][6];
            for(int i = 0; i < hands.length; i++){
                newHands[i] = hands[i];
            }
        }
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
}