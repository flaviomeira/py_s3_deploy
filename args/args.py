def configure_parser(parser):
    parser.add_argument('--local-path',
                        '-P',
                        type=str,
                        help='Path to be deployed')

    parser.add_argument('--bucket-name',
                        '-b',
                        type=str,
                        help='Bucket to deploy to')

    return parser.parse_args()