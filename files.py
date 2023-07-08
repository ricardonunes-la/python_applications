def main():
    # Open a file for writing and create it if it doesn't exist
    file_handle = open("my_file.txt", "w+")

    # Write some lines of data to the file
    for i in range(10):
        file_handle.write("This is line %d\n" % (i+1))

    # Close the file when done
    file_handle.close()

    # Open the file back up and read the contents
    file_handle = open("my_file.txt", "r")
    if file_handle.mode == 'r':  # Check if the file was opened in read mode
        # Read the individual lines of the file into a list
        lines = file_handle.readlines()

        # Print each line of the file
        for line in lines:
            print(line.strip())  # Strip the newline character

if __name__ == "__main__":
    main()
