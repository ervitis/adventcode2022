def main():
    buffer = []
    
    counter = 0
    with open('../data', 'r') as fp:
        i = 0
        while True:
            c = fp.read(1)
            if not c:
                break
            if i < 4:
                buffer.append(c)
                i += 1
            if len(set(buffer)) == 4:
                break
            if i == 4:
                buffer = buffer[-1:] + buffer[:-1]
                buffer[3] = c
            counter += 1
    print(counter)


if __name__ == '__main__':
    main()
