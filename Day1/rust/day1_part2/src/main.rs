use std::fs::File;
use std::io::{BufRead, BufReader};

const START_NUMBER: i64 = 50;
const INPUT_FILE: &str = "../../input/input.txt";

fn main() 
{
    let file = File::open(INPUT_FILE).expect("Cannot open file");
    let reader = BufReader::new(file);

    let mut counter: i64 = START_NUMBER;
    let mut zero_counter: i64 = 0;
    let mut remainder: i64;

    for line in reader.lines() 
    {
        let input: String = line.unwrap();
        let direction: char = input.chars().nth(0).unwrap();
        let direction_int: i8 = if direction == 'R' { 1 } else { -1 };
        let line_number: i64 = input[1..].parse().unwrap();
        let prev_counter = counter;

        zero_counter += line_number / 100;
        remainder = line_number % 100;

        counter += direction_int as i64 * remainder;

        if counter <= 0 && prev_counter != 0
        {
            zero_counter += 1;
        }
        else if counter >= 100 
        {
            zero_counter += 1;
        }

        counter = ((counter % 100) + 100) % 100;

        //println!("Prev: {}, entry: {}{} New:{} Total zeros: {}", prev_counter, direction, line_number, counter, remainder, zero_counter);
    }
    println!("Final Zero Counter: {}", zero_counter);
}