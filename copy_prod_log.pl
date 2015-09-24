#!/usr/bin/perl -w

my $host_list=$ARGV[0];
my @hosts=`cat $host_list`;
my $date=`date -d "1 days ago" +%Y%m%d`;
my $hostname=`hostname`;
$hostname  =~ s/\R//g;
my $keychain_file = $hostname . "-sh";
$date  =~ s/\R//g;

my $log_root="/home/shengwu/log";
if ( ! -d $log_root ) { mkdir $log_root; }
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

  my @files=` source ~/.keychain/$keychain_file; /usr/bin/ssh -o 'StrictHostKeyChecking no' shengwu\@$host 'find /home/y/logs/vespa/accesslog/access.log.* -daystart -mtime -2 -mtime +0 -type f' `;

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
      `scp $host:$file $log_dir/`;
    }
  }
  print "\n";
}
