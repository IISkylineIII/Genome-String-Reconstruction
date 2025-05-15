ef reconstruct_string(paired_reads):
    def overlap(s1, s2):
        for i in range(1, len(s1)):
            if s1[i:] == s2[:len(s1) - i]:
                return i
        return 0

    def merge_strings(s1, s2, olen):
        return s1 + s2[olen:]

    while len(paired_reads) > 1:
        found_overlap = False
        for i, read1 in enumerate(paired_reads):
            for j, read2 in enumerate(paired_reads):
                if i != j:
                    olen = overlap(read1[0], read2[0])
                    if olen > 0:
                        paired_reads.pop(i)
                        paired_reads.pop(j - 1)
                        paired_reads.append((merge_strings(read1[0], read2[0], olen), merge_strings(read1[1], read2[1], olen)))
                        found_overlap = True
                        break
            if found_overlap:
                break

    return paired_reads[0][0] + paired_reads[0][1][-(len(paired_reads[0][1]) - k - d):]

paired_reads = [('ACC', 'ATA'), ('ACT', 'ATT'), ('ATA', 'TGA'), ('ATT', 'TGA'), ('CAC', 'GAT'), ('CCG', 'TAC'),
                ('CGA', 'ACT'), ('CTG', 'AGC'), ('CTG', 'TTC'), ('GAA', 'CTT'), ('GAT', 'CTG'), ('GAT', 'CTG'),
                ('TAC', 'GAT'), ('TCT', 'AAG'), ('TGA', 'GCT'), ('TGA', 'TCT'), ('TTC', 'GAA')]

print(result)
