function Decoder(bytes, port) {

  // Based on https://stackoverflow.com/a/37471538 by Ilya Bursov
  function bytesToFloat(bytes) {
    // JavaScript bitwise operators yield a 32 bits integer, not a float.
    // Assume LSB (least significant byte first).
    var bits = bytes[3]<<24 | bytes[2]<<16 | bytes[1]<<8 | bytes[0];
    var sign = (bits>>>31 === 0) ? 1.0 : -1.0;
    var e = bits>>>23 & 0xff;
    var m = (e === 0) ? (bits & 0x7fffff)<<1 : (bits & 0x7fffff) | 0x800000;
    var f = sign * m * Math.pow(2, e - 150);
    return f;
  }  

  return {
    temperature: bytesToFloat(bytes.slice(0, 4)).toFixed(2)
    pressure: (bytesToFloat(bytes.slice(4, 8))/100).toFixed(2)
    humidity: bytesToFloat(bytes.slice(8, 12)).toFixed(0)
  };
}
