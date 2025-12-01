use std::fs::File;
use std::io::{BufRead, BufReader};

const START_NUMBER: i64 = 50;

fn split_char_number(s: &str) -> Option<(char, i64)> {
    let mut chars = s.chars();
    let first_char = chars.next()?;
    let number_str: String = chars.collect();
    let number = number_str.parse::<i64>().ok()?;
    Some((first_char, number))
}

fn main() {
    let file = File::open("../../input/input.txt").expect("Cannot open file");
    let reader = BufReader::new(file);

    let mut counter: i64 = START_NUMBER;
    let mut zero_counter: i64 = 0;

    for line in reader.lines() {
        let string_part: &str = &line.as_ref().unwrap();
        if let Some((c , n)) = split_char_number(string_part) 
        {
            println!("Character: {}, Number: {}", c, n);
            if c == 'R' 
            {
                counter += n;
            } 
            else if c == 'L' 
            {
                counter -= n;
            }
        }
        else
        {
            eprintln!("Failed to parse line: {}", string_part);
        }

        counter %= 100;

        if counter == 0
        {
            zero_counter += 1;
        }

        println!("Counter: {}, Zero Counter: {}", counter, zero_counter);
    }
}