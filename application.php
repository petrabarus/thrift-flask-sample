<?php

require 'vendor/autoload.php';

use Thrift\Protocol\TBinaryProtocol;
use Thrift\Transport\TSocket;
use Thrift\Transport\THttpClient;
use Thrift\Transport\TBufferedTransport;
use Thrift\Exception\TException;

try {
    $socket = new THttpClient('localhost', 5000);
    $transport = new TBufferedTransport($socket, 1024, 1024);
    $protocol = new TBinaryProtocol($transport);
    $client = new \petrabarus\GeometryClient($protocol);
    $transport->open();

    $point1 = new \petrabarus\Point(['x' => 1, 'y' => 1]);
    $point2 = new \petrabarus\Point(['x' => 2, 'y' => 2]);

    $distance = $client->distance($point1, $point2);

    print "Distance is : {$distance}\n";

} catch (TException $tx) {
    print "TException: {$tx->getMessage()}\n";
}
