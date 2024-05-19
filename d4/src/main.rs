use std::env;
use std::fs;

fn parse_line(line: &str) -> ((i32, i32), (i32, i32)) {
    let mut parts = line.split(',');

    let range_1 = parts.next().unwrap();
    let mut range_1_parts = range_1.split("-");

    let min_1 = range_1_parts.next().unwrap().parse::<i32>().unwrap();
    let max_1 = range_1_parts.next().unwrap().parse::<i32>().unwrap();
    let range_2 = parts.next().unwrap();
    let mut range_2_parts = range_2.split("-");

    let min_2 = range_2_parts.next().unwrap().parse::<i32>().unwrap();
    let max_2 = range_2_parts.next().unwrap().parse::<i32>().unwrap();

    return ((min_1, max_1), (min_2, max_2));
}
fn main() {
    let args: Vec<String> = env::args().collect();

    let filepath = &args[1];
    let contents = fs::read_to_string(filepath);

    let contents = contents.expect("Something went wrong reading the file");

    let lines = contents.lines();

    let mut count = 0;

    lines.for_each(|line| {
        let ((min_1, max_1), (min_2, max_2)) = parse_line(line);
        if max_1 >= min_2 && min_1 <= max_2 {
            count += 1;
        }
    });
    println!("count: {}", count)
}
