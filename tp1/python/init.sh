if [ -z "$1" ]; then
	w=1
else
	w=$1
fi

echo "Usando $w workers"
gunicorn app:app -w $w
