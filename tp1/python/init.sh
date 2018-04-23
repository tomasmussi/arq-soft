if [ -z "$1" ]; then
	port=8000
else
	port=$1
fi

if [ -z "$2" ]; then
	w=1
else
	w=$2
fi


echo "Binding en puerto $port, usando $w workers"
gunicorn app:app -w $w -b 127.0.0.1:$port
