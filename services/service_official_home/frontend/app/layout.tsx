import type { Metadata } from 'next';
import { Inter } from 'next/font/google';
import './globals.css';

const inter = Inter({ subsets: ['latin'] });

export const metadata: Metadata = {
  title: {
    default: '현사AI - 현명한 사람들의 AI',
    template: '%s | 현사AI',
  },
  description: 'AI를 모르는 사람들과 AI 공부가 귀찮은 사람들을 위한 AI 산출물 공급 서비스. AI 이미지 생성, 동화책 제작, 업무 자동화를 쉽고 빠르게.',
  keywords: ['AI', '인공지능', '이미지 생성', '동화책', '업무 자동화', '현사AI', 'Smart Person AI'],
  authors: [{ name: 'Smart Person AI Team' }],
  creator: 'Smart Person AI',
  publisher: 'Smart Person AI',
  
  // Open Graph / Facebook
  openGraph: {
    type: 'website',
    locale: 'ko_KR',
    url: 'https://smartpersonai.com',
    title: '현사AI - 현명한 사람들의 AI',
    description: 'AI 시대의 현명한 사람들은 AI 사용자가 될 것을 나는 믿는다. 현사AI와 함께 AI를 쉽게 활용하세요.',
    siteName: '현사AI',
    images: [
      {
        url: '/og-image.png',
        width: 1200,
        height: 630,
        alt: '현사AI - 현명한 사람들의 AI',
      },
    ],
  },
  
  // Twitter
  twitter: {
    card: 'summary_large_image',
    title: '현사AI - 현명한 사람들의 AI',
    description: 'AI를 쉽고 빠르게 활용할 수 있는 모든 서비스를 한 곳에서',
    images: ['/twitter-image.png'],
    creator: '@smartpersonai',
  },
  
  // 기타 메타데이터
  robots: {
    index: true,
    follow: true,
    googleBot: {
      index: true,
      follow: true,
      'max-video-preview': -1,
      'max-image-preview': 'large',
      'max-snippet': -1,
    },
  },
  
  // 언어 설정
  alternates: {
    canonical: 'https://smartpersonai.com',
    languages: {
      'ko-KR': 'https://smartpersonai.com',
      'en-US': 'https://smartpersonai.com/en',
    },
  },
  
  // 모바일 최적화
  viewport: {
    width: 'device-width',
    initialScale: 1,
    maximumScale: 1,
  },
  
  // 애플리케이션
  applicationName: '현사AI',
  appleWebApp: {
    capable: true,
    statusBarStyle: 'default',
    title: '현사AI',
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="ko" className="scroll-smooth">
      <head>
        {/* 추가 메타 태그 */}
        <meta name="theme-color" content="#2563eb" />
        <meta name="apple-mobile-web-app-capable" content="yes" />
        <meta name="apple-mobile-web-app-status-bar-style" content="default" />
        <meta name="apple-mobile-web-app-title" content="현사AI" />
        
        {/* 파비콘 */}
        <link rel="icon" href="/favicon.ico" />
        <link rel="apple-touch-icon" href="/apple-touch-icon.png" />
        
        {/* Google Analytics */}
        {process.env.NODE_ENV === 'production' && (
          <>
            <script
              async
              src={`https://www.googletagmanager.com/gtag/js?id=${process.env.NEXT_PUBLIC_GA_ID}`}
            />
            <script
              dangerouslySetInnerHTML={{
                __html: `
                  window.dataLayer = window.dataLayer || [];
                  function gtag(){dataLayer.push(arguments);}
                  gtag('js', new Date());
                  gtag('config', '${process.env.NEXT_PUBLIC_GA_ID}');
                `,
              }}
            />
          </>
        )}
      </head>
      <body className={inter.className}>
        {children}
        
        {/* 구조화된 데이터 (SEO) */}
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{
            __html: JSON.stringify({
              '@context': 'https://schema.org',
              '@type': 'Organization',
              name: '현사AI',
              alternateName: 'Smart Person AI',
              url: 'https://smartpersonai.com',
              logo: 'https://smartpersonai.com/logo.png',
              description: 'AI를 모르는 사람들과 AI 공부가 귀찮은 사람들을 위한 AI 산출물 공급 서비스',
              sameAs: [
                'https://twitter.com/smartpersonai',
                'https://linkedin.com/company/smartpersonai',
              ],
              contactPoint: {
                '@type': 'ContactPoint',
                telephone: '+82-10-0000-0000',
                contactType: 'customer service',
              },
            }),
          }}
        />
      </body>
    </html>
  );
}