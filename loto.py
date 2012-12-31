import random

YEARS = 60
WEEKS_IN_YEAR = 52
TURNS_PER_WEEK = 2

def main():
  turns = YEARS * WEEKS_IN_YEAR * TURNS_PER_WEEK
  print 'Turns: %s' % turns
  
  my_nums = set([2, 6, 7, 8, 21, 28])
  wins = [0, 0, 0, 0, 0, 0, 0]
  
  while turns > 0:
    balls = set()
    while len(balls) < 6:
      balls.add(random.randint(1, 49))
  
    matches = my_nums.intersection(balls)
    wins[len(matches)] += 1
    turns -= 1
  
  print 'No Wins: %s' % wins[0]
  print '3 Balls: %s (%s)' % (wins[3], wins[3] * 10)
  print '4 Balls: %s' % wins[4]
  print '5 Balls: %s' % wins[5]
  print '6 Balls: %s' % wins[6]

if __name__ == '__main__':
  main()