def configure_parser(parser):
    parser.add_argument('--local-path',
                        '-P',
                        type=str,
                        help='Path to be deployed',
                        required=True)

    parser.add_argument('--bucket-name',
                        '-b',
                        type=str,
                        help='Bucket to deploy to',
                        required=True)

    parser.add_argument('--delete-removed',
                        '-d',
                        help='Delete local removed files from bucket',
                        action='store_true',
                        required=False)

    parser.add_argument('--verbose',
                        '-v',
                        help='Prints out on the console what is happening',
                        action='store_true',
                        required=False,
                        default=False)

    return parser.parse_args()
