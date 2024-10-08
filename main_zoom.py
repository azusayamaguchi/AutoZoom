if __name__ == '__main__':

    import PyZoom as PZ
    import argparse

    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description="Pass meeting details as arguments.")

    # Add arguments
    parser.add_argument("--MeetingID", required=True, help="Meeting ID (e.g., '880 1935 6472')")
    parser.add_argument("--Passcode", default=None, help="Passcode for the meeting (optional)")
    parser.add_argument("--MeetingTime", required=True, help="Time of the meeting (e.g., '0.5m')")
    args = parser.parse_args()

    print(args.MeetingID,args.MeetingTime,args.Passcode)
    PZ.AutoZoom(args.MeetingID,args.MeetingTime,Passcode=args.Passcode)

