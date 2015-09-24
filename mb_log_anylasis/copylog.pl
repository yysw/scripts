#!/usr/bin/perl -w
my @hosts=`cat ./slingstone_bf1.txt`;

my $count=0;
foreach(@hosts)
{
  my $host = $_;
  chomp $host;
  $host =~ s/^\s+//; #remove leading spaces
  $count += 1;
  if ( $count >  80) { last; }
  print " $count\n";

  my  $log_dir="log/$host";
  if ( ! -d $log_dir ) 
  { 
    mkdir $log_dir; 
  } 
  else 
  {
    next;
  }

  my @files=`yinst ssh 'find /home/y/logs/vespa/vespa* -mtime -5 -type f' -h $host `;

  foreach(@files)
  {
    my $file = $_;
    chomp $file;
    #print "$log_dir\n";
    print "$host:$file\n";
    `scp $host:$file $log_dir`;
  }
  print "\n";
}
