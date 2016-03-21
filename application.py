"""
Based on https://gist.github.com/BeanYoung/8318363
"""

import sys
import math

sys.path.append('gen-py')

from flask import Flask, request, make_response
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from thrift.transport import TTransport
from petrabarus import Geometry

class GeometryHandler:
    def distance(self, a, b):
        return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)

handler = GeometryHandler()
processor = Geometry.Processor(handler)
protocol = TBinaryProtocol.TBinaryProtocolFactory()
server = TServer.TServer(processor, None, None, None, protocol, protocol)

app = Flask(__name__)

@app.route('/', methods=['POST'])
def service():
    itrans = TTransport.TMemoryBuffer(request.data)
    otrans = TTransport.TMemoryBuffer()
    iprot = server.inputProtocolFactory.getProtocol(itrans)
    oprot = server.outputProtocolFactory.getProtocol(otrans)
    server.processor.process(iprot, oprot)
    return make_response(otrans.getvalue())

if __name__ == '__main__':
    app.run()
