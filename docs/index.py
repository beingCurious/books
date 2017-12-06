#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

base = os.path.expanduser('./src')
topics = [f for f in os.listdir(base) if os.path.isdir(os.path.join(base, f))]

f = open(os.path.expandvars('./INDEX.md'), 'w')

f.write('Booklist\n')
f.write('========\n\n')

for topic in topics:
    f.write("### %s\n\n" % topic)
    f.write("%-20s | %s\n" % ('Topic', 'Title'))
    f.write("%-20s | %s\n" % (':---:', ':---'))

    topic_dir = base + '/' + topic
    files = os.listdir(topic_dir)
    for file in files:
        if file.endswith('.DS_Store'):
            continue
        title = os.path.splitext(file)[0].replace('-', ' ')
        line = "%-20s | [%s](src/%s/%s)\n" % (topic, title, topic, file)
        f.write(line)
    f.write('\n')

f.close()

print('INDEX.md has been updated (created) successfully.')
