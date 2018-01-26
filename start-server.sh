$CERT=cert.pem
if [ -f $CERT ]; then
   echo "Certificate $CERT exists."
else
   echo "Gnerate $CERT"
   openssl req -new -x509 -keyout cert.pem -out cert.pem -days 365 -nodes
fi


python server.py

