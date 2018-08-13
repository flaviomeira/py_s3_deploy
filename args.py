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
                        help='Delete removed files.',
                        action='store_true',
                        required=False)

    return parser.parse_args()
