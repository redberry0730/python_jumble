import numpy

def galileo(d, a, b):
    runs = pow((2 * pow(6, d)), 2);
    arr = numpy.random.randint(1, 7, size = (runs, d));
    columns = arr.sum(axis = 1);

    match_a = numpy.equal(columns, a);
    match_b = numpy.equal(columns, b);

    count_a = numpy.count_nonzero(match_a);
    count_b = numpy.count_nonzero(match_b);

    raw_a = count_a / runs;
    raw_b = count_b / runs;

    estimated_a = round(raw_a * (pow(6, d)));
    estimated_b = round(raw_b * (pow(6, d)));

    if (estimated_a > estimated_b):
        return 1;
    elif (estimated_a == estimated_b):
        return 0;
    else:
        return -1;