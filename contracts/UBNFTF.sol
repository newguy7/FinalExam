//SPDX-License-Identifier: MIT

pragma solidity 0.7.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "./UBFToken.sol";

contract UBNFTF is ERC721 {
    uint256 public tokenCounter;
    uint256 public maxLogos = 5;
    uint256 public tokenFee;
    UBFToken ubftoken;

    mapping(uint256 => address) public requestIdToSender;

    event requestedLogo(uint256 indexed requestId, address requester);

    constructor(address _ubftokenAddress) ERC721("Final Exam NFT", "UBNFTF") {
        ubftoken = UBFToken(_ubftokenAddress);
        uint8 tokenDecimals = ubftoken.decimals();
        tokenFee = 1000 * (10**tokenDecimals);
        tokenCounter = 0;
    }

    function checkTokenBalance() public view returns (uint256) {
        return ubftoken.balanceOf(address(this));
    }

    function CreateLogoNFT(string memory _tokenURI) public returns (bytes32) {
        require(tokenCounter <= maxLogos, "Maximum number of Logos emitted!");
        require(
            tokenFee <= ubftoken.balanceOf(address(this)),
            "Not enough fund!"
        );

        uint256 newTokenID = tokenCounter;
        requestIdToSender[newTokenID] = msg.sender;
        emit requestedLogo(newTokenID, msg.sender);

        _safeMint(msg.sender, newTokenID);
        _setTokenURI(newTokenID, _tokenURI);

        tokenCounter += 1;
    }
}
