START = 'from django.db import models\n\n\nclass Document(models.Model):\n    '

END = '   file = open("res.txt", "w")\n    print(folder, file=file)\n    docfile = models.FileField(upload_to="%s" % folder)\n    file.close()'