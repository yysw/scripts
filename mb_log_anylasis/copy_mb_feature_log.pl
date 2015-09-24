#!/usr/bin/perl -w

my @hosts=`cat /home/shengwu/fdp.txt`;
my $date=`date -d "1 days ago" +%Y%m%d`;
$date  =~ s/\R//g;
my $log_root="/home/yahoo";
my $count=0;
foreach(@hosts)
{
  my $host = $_;
  chomp $host;
  $host =~ s/^\s+//; #remove leading spaces
  $count += 1;
#  if ( $count >  1) { last; }
  print " $count\n";

  my $log_dir_base="$log_root/$date";
  if ( ! -d $log_dir_base ) { mkdir $log_dir_base; }
  my  $log_dir="$log_dir_base/$host";
  if ( ! -d $log_dir ) { mkdir $log_dir; }

  my @files=` source ~/.keychain/cablestables.corp.-sh; /usr/bin/ssh -o 'StrictHostKeyChecking no' shengwu\@$host 'find /home/y/logs/archive-slingstone_moneyball_scoring_server/moneyball.feature.log.*.gz -daystart -mtime -2 -mtime +0 -type f' `;

  foreach(@files)
  {
    my $file = $_;
    chomp $file;
    $file  =~ s/\R//g;
    print "file: $file\n";
    my $basename = $file;
    $basename =~ s/\S+\///;
    my $target_file = $log_dir . "/" . $basename;
    if ( -e $target_file )
    {
      print ("skip existed file: $target_file\n");
      next;
    }
    else
    {
      print "copy $host:$file\n";
      `source ~/.keychain/cablestables.corp.ne1.yahoo.com-sh; /usr/bin/scp $host:$file $log_dir`;
    }
  }
  print "\n";
}
