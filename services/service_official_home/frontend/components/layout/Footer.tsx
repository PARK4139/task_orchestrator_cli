'use client';

import Link from 'next/link';
import { 
  MailIcon, 
  PhoneIcon, 
  MapPinIcon,
  TwitterIcon,
  LinkedinIcon,
  GithubIcon
} from 'lucide-react';

const Footer = () => {
  const currentYear = new Date().getFullYear();

  const footerLinks = {
    서비스: [
      { name: 'AI 이미지 생성', href: '/services/ai-image' },
      { name: 'AI 동화책 생성', href: '/services/ai-book' },
      { name: '엑셀 자동화', href: '/services/excel-automation' },
      { name: '웹 크롤링', href: '/services/web-crawler' },
    ],
    회사: [
      { name: '회사 소개', href: '/about' },
      { name: '팀', href: '/team' },
      { name: '채용', href: '/careers' },
      { name: '블로그', href: '/blog' },
    ],
    지원: [
      { name: '도움말', href: '/help' },
      { name: 'API 문서', href: '/docs' },
      { name: '커뮤니티', href: '/community' },
      { name: '문의하기', href: '/contact' },
    ],
    법적사항: [
      { name: '이용약관', href: '/terms' },
      { name: '개인정보처리방침', href: '/privacy' },
      { name: '쿠키 정책', href: '/cookies' },
      { name: '환불 정책', href: '/refund' },
    ],
  };

  return (
    <footer className="bg-slate-900 text-white">
      {/* 메인 푸터 콘텐츠 */}
      <div className="container-custom py-16">
        <div className="grid md:grid-cols-2 lg:grid-cols-6 gap-8">
          {/* 회사 정보 */}
          <div className="lg:col-span-2">
            <div className="mb-6">
              <h3 className="text-2xl font-bold mb-2">현사AI</h3>
              <p className="text-slate-400 mb-4">
                현명한 사람들의 AI
              </p>
              <blockquote className="text-slate-300 italic text-sm leading-relaxed border-l-2 border-blue-500 pl-4">
                "AI 시대의 현명한 사람들은<br />
                AI 사용자가 될 것을 나는 믿는다."
              </blockquote>
            </div>

            {/* 연락처 정보 */}
            <div className="space-y-3 text-sm text-slate-400">
              <div className="flex items-center">
                <MailIcon className="w-4 h-4 mr-3" />
                <a href="mailto:contact@smartpersonai.com" className="hover:text-white transition-colors">
                  contact@smartpersonai.com
                </a>
              </div>
              <div className="flex items-center">
                <PhoneIcon className="w-4 h-4 mr-3" />
                <a href="tel:+82-1588-0000" className="hover:text-white transition-colors">
                  1588-0000
                </a>
              </div>
              <div className="flex items-center">
                <MapPinIcon className="w-4 h-4 mr-3" />
                <span>서울특별시 강남구 테헤란로 123</span>
              </div>
            </div>

            {/* 소셜 미디어 */}
            <div className="flex space-x-4 mt-6">
              <a 
                href="https://twitter.com/smartpersonai" 
                className="p-2 bg-slate-800 rounded-lg hover:bg-slate-700 transition-colors"
                aria-label="Twitter"
              >
                <TwitterIcon className="w-5 h-5" />
              </a>
              <a 
                href="https://linkedin.com/company/smartpersonai" 
                className="p-2 bg-slate-800 rounded-lg hover:bg-slate-700 transition-colors"
                aria-label="LinkedIn"
              >
                <LinkedinIcon className="w-5 h-5" />
              </a>
              <a 
                href="https://github.com/smartpersonai" 
                className="p-2 bg-slate-800 rounded-lg hover:bg-slate-700 transition-colors"
                aria-label="GitHub"
              >
                <GithubIcon className="w-5 h-5" />
              </a>
            </div>
          </div>

          {/* 링크 섹션들 */}
          {Object.entries(footerLinks).map(([category, links]) => (
            <div key={category}>
              <h4 className="font-semibold text-white mb-4">{category}</h4>
              <ul className="space-y-3">
                {links.map((link) => (
                  <li key={link.name}>
                    <Link 
                      href={link.href}
                      className="text-slate-400 hover:text-white transition-colors text-sm"
                    >
                      {link.name}
                    </Link>
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>
      </div>

      {/* 뉴스레터 구독 섹션 */}
      <div className="border-t border-slate-800">
        <div className="container-custom py-8">
          <div className="flex flex-col md:flex-row items-center justify-between">
            <div className="mb-4 md:mb-0">
              <h4 className="font-semibold text-white mb-2">현사AI 소식을 받아보세요</h4>
              <p className="text-slate-400 text-sm">
                새로운 AI 서비스와 특별 혜택을 가장 먼저 알려드립니다.
              </p>
            </div>
            <form className="flex w-full md:w-auto">
              <input
                type="email"
                placeholder="이메일 주소"
                className="flex-1 md:w-80 px-4 py-2 bg-slate-800 border border-slate-700 rounded-l-lg focus:outline-none focus:ring-2 focus:ring-blue-500 text-white placeholder-slate-400"
              />
              <button
                type="submit"
                className="px-6 py-2 bg-blue-600 hover:bg-blue-700 rounded-r-lg transition-colors font-medium"
              >
                구독
              </button>
            </form>
          </div>
        </div>
      </div>

      {/* 하단 저작권 */}
      <div className="border-t border-slate-800">
        <div className="container-custom py-6">
          <div className="flex flex-col md:flex-row items-center justify-between text-sm text-slate-400">
            <div className="mb-4 md:mb-0">
              <p>© {currentYear} 현사AI (Smart Person AI). All rights reserved.</p>
            </div>
            <div className="flex items-center space-x-6">
              <span>사업자등록번호: 123-45-67890</span>
              <span>대표: 홍길동</span>
              <span>
                <span className="inline-block w-2 h-2 bg-green-500 rounded-full mr-2 animate-pulse"></span>
                서비스 정상 운영 중
              </span>
            </div>
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;