text = "X-DSPAM-Confidence:    0.8475";
stpos = text.find('0');
endpos = text.find('5');
value= float(text[stpos:endpos+1]);
print(value);
