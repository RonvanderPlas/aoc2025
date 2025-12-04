use std::fs::File;
use std::io::{BufRead, BufReader};

const INPUT_FILE: &str = "../../input/input.txt";

struct InputRange
{
    low: i64,
    high: i64,
}

fn read_file(file_path: &str, vec_input: &mut Vec<InputRange>) 
{
    let file = File::open(file_path).expect("Cannot open file");
    let reader = BufReader::new(file);
    for line in reader.lines() 
    {
        let line = line.unwrap();
        let parts: Vec<&str> = line.split(',').collect();
        for entry in parts 
        {
            let range_parts: Vec<&str> = entry.split('-').collect();
            if range_parts.len() == 2 
            {
                let low = range_parts[0].parse::<i64>().expect("Invalid number");
                let high = range_parts[1].parse::<i64>().expect("Invalid number");
                vec_input.push(InputRange { low, high });
            }
        }
    }
}
fn determine_pattern_within_range(pattern_length: i64, low: i64, high: i64) -> i64
{
    let mut invalid_counter = 0;
    let section_length = pattern_length / 2;
    let base: i64 = 10;
    let starting_range = base.pow((section_length - 1) as u32);
    let ending_range = base.pow(section_length as u32) - 1;
    for i in starting_range..=ending_range
    {
        let pattern = (i * base.pow(section_length as u32)) + i;
        if pattern >= low && pattern <= high
        {
            println!("Invalid pattern: {}", pattern);
            invalid_counter += pattern;
        }
    }
    return invalid_counter;
}

fn main() 
{
    let mut ranges: Vec<InputRange> = Vec::new();
    let mut total_count = 0;
    read_file(INPUT_FILE, &mut ranges);
    for range in ranges 
    {
        let low_len: usize = range.low.to_string().len();
        let high_len: usize = range.high.to_string().len();
        let pattern_length = std::cmp::max(low_len, high_len);

        total_count += determine_pattern_within_range(pattern_length as i64, range.low, range.high);
    }
    println!("Total invalid patterns: {}", total_count);
}
